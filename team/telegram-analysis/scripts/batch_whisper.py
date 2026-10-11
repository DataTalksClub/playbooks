"""Batch-transcribe Telegram voice messages with faster-whisper (CPU int8, small model)."""
import os
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
import json, sys, glob, subprocess
import numpy as np
from multiprocessing import Pool

MODEL = None
MODEL_NAME = os.environ.get('WHISPER_MODEL', 'small')


def load_audio(file):
    # PyAV decode (no external binary needed); ffmpeg CLI fallback
    try:
        import av
        c = av.open(file)
        rs = av.AudioResampler(format='s16', layout='mono', rate=16000)
        chunks = []
        for fr in c.decode(audio=0):
            out = rs.resample(fr)
            if out and out[0] is not None:
                chunks.append(out[0].to_ndarray().reshape(-1))
        c.close()
        a = np.concatenate(chunks) if chunks else np.zeros(0, dtype=np.int16)
        return a.astype(np.float32) / 32768.0
    except Exception:
        out = subprocess.run(['ffmpeg', '-nostdin', '-threads', '0', '-i', file,
                              '-f', 's16le', '-ac', '1', '-ar', '16000', '-'],
                             capture_output=True).stdout
        return np.frombuffer(out, np.int16).astype(np.float32) / 32768.0


def init_worker():
    global MODEL
    from faster_whisper import WhisperModel
    MODEL = WhisperModel(MODEL_NAME, device='cpu', compute_type='int8', cpu_threads=1)


def transcribe(path):
    out = path + '.json'
    if os.path.exists(out):
        return 'skip'
    try:
        audio = load_audio(path)
        if len(audio) < 1600:
            rec = {'file': os.path.basename(path), 'language': None, 'text': ''}
            with open(out, 'w') as f:
                json.dump(rec, f, ensure_ascii=False)
            return 'empty'
        segs, info = MODEL.transcribe(audio, vad_filter=False, condition_on_previous_text=False)
        text = ' '.join(s.text.strip() for s in segs)
        rec = {'file': os.path.basename(path), 'language': info.language, 'text': text}
        with open(out, 'w') as f:
            json.dump(rec, f, ensure_ascii=False)
        return 'ok'
    except Exception as e:
        with open(out + '.err', 'w') as f:
            f.write(str(e))
        return 'err:' + str(e)[:100]


if __name__ == '__main__':
    indir = sys.argv[1]
    order = sys.argv[2] if len(sys.argv) > 2 else 'newest'
    # newest first: voice file numbering increases over time, so reverse sort
    # puts the most recent months at the front of the queue
    files = sorted(glob.glob(os.path.join(indir, '**', '*.ogg'), recursive=True), reverse=(order == 'newest'))
    print(f'{len(files)} files', flush=True)
    # pre-download/load the model once so pool workers hit the cache
    from faster_whisper import WhisperModel
    WhisperModel(MODEL_NAME, device='cpu', compute_type='int8', cpu_threads=1)
    with Pool(6, initializer=init_worker) as pool:
        for i, res in enumerate(pool.imap_unordered(transcribe, files, chunksize=4), 1):
            if i % 25 == 0 or res.startswith('err'):
                print(f'[{i}/{len(files)}] {res}', flush=True)
    print('DONE', flush=True)
