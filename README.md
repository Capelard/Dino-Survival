# Dino Survival - Railway Deploy

## Deploy (about 2 minutes)
1. Create a GitHub repo (example: Capelard/dino-survival). Push this folder's contents to the repo root.
2. Railway dashboard: New Project, then Deploy from GitHub repo, pick the repo. Railway detects Node and runs npm start automatically.
3. In the service: Settings, then Networking, then Generate Domain. That URL is the game.

## Install on the boys' tablets like an app
1. Open the Railway URL in Safari (iPad) or Chrome (Android).
2. Safari: Share button, then Add to Home Screen. Chrome: menu, then Add to Home screen.
3. Launches fullscreen with the T-Rex icon. Works offline after first load (service worker cache).

## Notes
- Saves are per device (browser localStorage). Each kid's tablet keeps its own progress.
- To ship an update: change the file, push to GitHub, Railway redeploys automatically. Bump the cache name in sw.js (dino-survival-v14) so devices pull the new version.

## Deploy pipeline
Automated: Claude pushes updates to this repo, Railway redeploys automatically. Verified 2026-07-04.
