# מדריך עבודה עבודה עם בסיס נתונים PostgreSQL באמצעות Docker.


## התקנה

1. הורד והתקן את Docker Desktop:
   - [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## שימוש ב־Volumes

Volumes מנוהלים על ידי Docker ומספקים דרך אמינה לאחסן נתונים, אפילו אם הקונטיינר נמחק.

צור ווליום לדאטה:

```bash
docker volume create mydbdata
```


