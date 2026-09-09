from dataclasses import dataclass
import requests

@dataclass
class ApiClient:
    base_url: str
    token: str | None = None

    def _headers(self) -> dict[str, str]:
        if not self.token:
            return {}
        return {"Authorization": f"Bearer {self.token}"}

    def get(self, path: str) -> requests.Response:
        return requests.get(f"{self.base_url}{path}", headers=self._headers(), timeout=10)

    def post(self, path: str, payload: dict) -> requests.Response:
        return requests.post(f"{self.base_url}{path}", json=payload, headers=self._headers(), timeout=10)
