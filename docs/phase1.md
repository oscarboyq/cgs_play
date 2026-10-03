# Phase 1: Android viewer and publishing foundation

Build one complete path from an owner's published drama to a customer's playable episode, saved progress, and resume. The admin app is a separate Flutter web application that uses the same Django API.

## Work order

1. Local PostgreSQL and backend environment; verify initial account migration.
2. Account flows: email/password first, then Google and Facebook one at a time for Android. The identity model also supports Apple; add and test Apple sign-in when the iOS app is built. Release only provider buttons that work end to end.
3. Admin sign-in, drama/episode metadata, video upload, processing status, and publish controls.
4. Android splash and sign-in/sign-up pages.
5. Home, categories, search, drama details, and episode list.
6. Vertical playback, watch progress, Continue Watching, My List, and History.
7. Profile, account deletion, settings, and support.

The locked episode, coins, ads, VIP purchases, and offline downloads depend on later entitlement, billing, and download flows. Do not show their controls as working features until those flows exist.

## Data boundaries

Use one internal `User` ID across apps. `AuthIdentity` stores one verified provider subject per external login. Customer registration cannot assign staff roles. Catalog, video storage, publication, progress, and watchlist models will be added as their implementation slices begin.

Uploaded videos and credentials stay outside Git. The API checks access before playback; media is delivered through object storage and a CDN.
