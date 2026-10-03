# CGS Play

The Phase 1 workspace contains three applications in one Git repository:

| Directory | Purpose |
| --- | --- |
| `django/` | Django REST API and PostgreSQL models |
| `flutter/viewer/` | Android customer app |
| `flutter/admin/` | Separate Flutter web admin app |

Video assets belong in object storage, not in Git. The planned delivery path is S3 upload, transcoding, and CDN playback. Social sign-in, content publishing, and playback are not implemented by this initial scaffold.

## Local setup

The source layout is ready. To run the backend, first install and start PostgreSQL, create a `cgs_play` database and role, and put their credentials in `django/.env`. Do not commit that file.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r django/requirements.txt
cp django/.env.example django/.env
# Edit django/.env with your local PostgreSQL credentials.
cd django
set -a; . ./.env; set +a
../.venv/bin/python manage.py migrate
../.venv/bin/python manage.py runserver
```

In separate terminals, run `flutter pub get` within each Flutter application. Run `flutter/viewer/` on an Android device or emulator and `flutter/admin/` in a browser.

The backend uses a custom user model from its first migration. Social provider identities are separate records linked to that user. The viewer's Android application ID is `com.oscarboyq.cgsplay`. iOS support can be generated after the Android Phase 1 flow is complete.

See `docs/phase1.md` for the first implementation slices.
