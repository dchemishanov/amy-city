from typing import Optional

from ..schema.suggestions import SuggestionsResponse
from ..engine.engine import Engine

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/suggestions", response_model=SuggestionsResponse)
def get_suggestions(
    query: str = Query(
        ...,
        alias="q",
        title="Query",
        description="Query string for matching to the list of city names",
        min_length=1,
        max_length=50,
    ),
    latitude: Optional[float] = Query(
        None,
        title="User Latitude",
        description="Location latitude of the user",
        ge=-180.0,
        le=180.0,
    ),
    longitude: Optional[float] = Query(
        None,
        title="User Longitude",
        description="Location longitude of the user",
        ge=-180.0,
        le=180.0,
    ),
):
    engine = Engine([{}, {}])
    return {"suggestions": engine.match(query, latitude=latitude, longitude=longitude)}
