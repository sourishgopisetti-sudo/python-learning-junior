# API Usage: weather_api.py

This script uses the OpenWeatherMap API to fetch current weather data.

## Getting an API key

1. Go to [openweathermap.org/api](https://openweathermap.org/api)
2. Create a free account
3. Go to your account -> "My API keys"
4. Copy your default API key

Note: new API keys can take up to a couple of hours to activate.

## Setting up the script

Open `weather_api.py` and replace the placeholder with your real API key:

```python
api_key = "YOUR_API_KEY_HERE"
```

## Running the script

```bash
python weather_api.py
```

## Example output
City: London
Temperature: 14.2 C
Conditions: light rain

## Notes
- Do not commit your real API key to GitHub. Replace it with the placeholder
  before pushing any changes.
- If you get a 401 error, your key likely hasn't activated yet, or the key was
  copied incorrectly.