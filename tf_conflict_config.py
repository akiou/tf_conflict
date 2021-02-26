import os
import jnius_config

if not jnius_config.vm_running:
    jar_path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'tf_conflict', 'lib', 'tf_conflict-java.jar'))
    if jar_path not in jnius_config.get_classpath():
        jnius_config.add_classpath(jar_path)
