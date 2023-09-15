#!/bin/bash

# Print Hello, world!
echo "Hello, world!"

# Start countdown from 1000 to 0
for i in {1000..0}; do
  echo "$i seconds remaining."
  sleep 1
done

echo "Time's up!"
