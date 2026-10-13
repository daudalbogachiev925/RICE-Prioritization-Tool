from dataclasses import dataclass, asdict
import json

@dataclass
class Feature:
    name: str
    reach: float
    impact: float
    confidence: float
    effort: float

    @property
    def rice_score(self):
        if self.effort == 0:
            return 0
        return (self.reach * self.impact * self.confidence) / self.effort

def load_features(path="features.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Feature(**item) for item in data]

def save_features(features, path="features.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(x) for x in features], f, ensure_ascii=False, indent=2)

def prioritize(features):
    return sorted(features, key=lambda x: x.rice_score, reverse=True)
