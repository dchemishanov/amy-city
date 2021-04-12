from typing import Dict, List
from pydantic import BaseModel, Field


class Suggestion(BaseModel):
    name: str = Field(
        title="City Name",
        description="Name, region, and country of the suggested city",
        max_length=50,
    )
    latitude: float = Field(
        title="City Latitude", description="Latitude of the suggested city"
    )
    longitude: float = Field(
        title="City Longitude", description="Longitude of the suggested city"
    )
    score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        title="Likelihood Score",
        description="Score assigned from the model",
    )


class SuggestionsResponse(BaseModel):
    suggestions: List[Suggestion] = Field(title="Suggestions", default=[])
