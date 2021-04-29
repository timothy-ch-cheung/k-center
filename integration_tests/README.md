Generate base images:
```
./node_modules/.bin/cypress run --env type=base --config screenshotsFolder=cypress/snapshots/base
```

Run regression tests:
```
./node_modules/.bin/cypress run --env type=actual
```

Alternatively to run tests from GUI:
```
./node_modules/.bin/cypress open
```