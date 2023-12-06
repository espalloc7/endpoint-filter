# endpoint-filter
filters the endpoints using blacklist(or whitelist) method

# Usage
put endpoints in endpoints.txt, modify the code that what you want to filter, (e.g. '404' or 'not found' [case insensitive]) and you are good to go.

if you want to use one-liner bash script instead:

```
while read endpoint; do curl -s $endpoint | grep -iq '401' || echo $endpoint; done < endpoints.txt > alive.txt
```
