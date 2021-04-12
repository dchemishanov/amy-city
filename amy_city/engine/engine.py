from typing import Dict, List, Optional


class Engine:
    def __init__(self, data: List[Dict]):
        self.data = data

    @staticmethod
    def _is_candidate(city: Dict, query: str) -> bool:
        """
        Simple euristics for sifting through the candidates.
        """
        return query.lower() in city.get("name", "").lower()

    @staticmethod
    def _score(
        city, query: str, latitude: Optional[float], longitude: Optional[float]
    ) -> float:
        """
        Score the probability of a city based on all available data.
        """
        distance_from_name_start = city.get("name", "").lower().index(query.lower())
        return 1/(distance_from_name_start+1)

    @staticmethod
    def _get_full_city_name(city: Dict) -> str:
        """
        Build the full city name out of name, administrative region, and country.
        """
        return city.get("name", "")

    def match(
        self,
        query: str,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
    ) -> List[Dict]:
        """
        Filter the data for matching cities and assign them appropriate scores.
        """
        suggestions = []
        for city in self.data:
            if self._is_candidate(city, query):
                suggestions.append(
                    {
                        "name": self._get_full_city_name(city),
                        "latitude": city.get("latitude", 0.0),
                        "longitude": city.get("longitude", 0.0),
                        "score": self._score(city, query, latitude, longitude),
                    }
                )
        return sorted(suggestions, reverse=True, key=lambda x: x["score"])
