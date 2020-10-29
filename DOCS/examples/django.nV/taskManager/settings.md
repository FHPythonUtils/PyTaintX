# settings

> Auto-generated documentation for [examples.django.taskManager.settings](../../../../examples/django.nV/taskManager/settings.py) module.

- [Pytaintx](../../../README.md#pytaintx-index) / [Modules](../../../README.md#pytaintx-modules) / `examples` / `django` / [taskManager](index.md#taskmanager) / settings

#### Attributes

- `SECRET_KEY` - SECURITY WARNING: keep the secret key used in production secret!: `'0yxzudryd8)-%)(fz&7q-!v&cq1u6vbfoc4u7@u_&i)b@4eh^q'`
- `DEBUG` - A5: Security Misconfiguration
  SECURITY WARNING: don't run with debug turned on in production!: `True`
- `PASSWORD_HASHERS` - A6: Sensitive Data Exposure: `['django.contrib.auth.hashers.MD5PasswordHasher']`
- `SESSION_ENGINE` - A2: Broken Auth and Session Management: `'django.contrib.sessions.backends.signed_cookies'`
- `SESSION_SERIALIZER` - Needs compatibility with older Django!: `'django.contrib.sessions.serializers.PickleSerializer'`
