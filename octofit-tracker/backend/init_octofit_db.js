// MongoDB initialization script for octofit_db

// Assumes the script is run with the context of the 'octofit_db' database

// Create users collection with unique email index
if (!db.getCollectionNames().includes('users')) {
  db.createCollection('users');
}
db.users.createIndex({ "email": 1 }, { unique: true });

// Create teams collection
if (!db.getCollectionNames().includes('teams')) {
  db.createCollection('teams');
}

// Create activity collection
if (!db.getCollectionNames().includes('activity')) {
  db.createCollection('activity');
}

// Create leaderboard collection
if (!db.getCollectionNames().includes('leaderboard')) {
  db.createCollection('leaderboard');
}

// Create workouts collection
if (!db.getCollectionNames().includes('workouts')) {
  db.createCollection('workouts');
}
