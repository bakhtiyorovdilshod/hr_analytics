set -e

mongo <<EOF
db = db.getSiblingDB('hr_analytics')

db.createUser({
  user: 'root',
  pwd: 'rootpassword',
  roles: [{ role: 'readWrite', db: 'hr_analytics' }],
});
db.createCollection('events')
EOF