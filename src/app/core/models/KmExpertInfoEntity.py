from pydantic import BaseModel, Field
from typing import List, Optional, TypedDict

class ServiceItem(TypedDict):
    service_name: str
    service_counts: int
    review_counts: int
    serice_page_url: str

class KmExpertInfoEntity(BaseModel):
    user_name: str
    user_page_url: str
    total_work_counts: int
    total_review_counts: int
    service_items: List[ServiceItem]
    
    # daily_work_counts: int #추후 추가예정
    
    