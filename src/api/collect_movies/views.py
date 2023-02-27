from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.containers import Container
from src.services.collect_movies_data_service import CollectMoviesDataService

router = APIRouter()


@router.post("/collect_movies_data")
@inject
def collect_and_store_movies_data_view(
        collect_service: CollectMoviesDataService = Depends(Provide[Container.collect_movies_data_service])
):
    collect_service.collect_and_store_movies_data()
