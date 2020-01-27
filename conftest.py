import os
from hypothesis import settings, Verbosity
settings.register_profile("debug", max_examples=1000000)
settings.register_profile("dev", max_examples=10)
settings.load_profile(os.getenv(u'HYPOTHESIS_PROFILE', 'debug'))
