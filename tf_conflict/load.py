import tf_conflict_config
from jnius import autoclass

def load():
    sample_cls = autoclass('aoka.sample.Sample')
    sample_ins = sample_cls()
