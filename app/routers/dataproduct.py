import random

from fastapi import APIRouter, Depends

from app.dependencies import verify_api_token
from app.models import CurrentWeatherMetricRequest, CurrentWeatherMetricResponse

# All APIs under this router verify any sent API tokens
router = APIRouter(dependencies=[Depends(verify_api_token)])


def get_weather_for_coords(lat: float, lon: float):
    _ = lat, lon
    humidity = min(random.uniform(0, 125), 100)  # nosec
    rain = humidity >= 99
    return {
        "rain": rain,
        "temp": random.uniform(-30, 40),  # nosec
        "pressure": random.uniform(870, 1083.8),  # nosec
        "humidity": humidity,
        "windSpeed": random.uniform(0, 100),  # nosec
        "windDirection": random.uniform(0, 360),  # nosec
    }


@router.post(
    "/Weather/Current/Metric_v1.0",
    summary="Current weather in a given location",
    description="Common data points about the current weather with metric units in a "
    "given location. Simplified for example use, and not following industry standards.",
    response_model=CurrentWeatherMetricResponse,
)
async def weather_current_metric(params: CurrentWeatherMetricRequest):
    return get_weather_for_coords(params.lat, params.lon)
