from dependency_injector import containers, providers

from application.use_cases.actions import ActionUseCase
from application.use_cases.analytics import AnalyticsUseCase
from application.use_cases.interfaces import IUseCase
from application.use_cases.kafka import KafkaConsumerUseCase
from infrastructure.repositories.actions import ActionRepository
from infrastructure.repositories.interfaces import IRepository


class Container(containers.DeclarativeContainer):
    action_repository: IRepository = providers.Factory(ActionRepository)
    action_use_case: IUseCase = providers.Factory(ActionUseCase, action_repository)
    analytics_use_case: AnalyticsUseCase = providers.Factory(
        AnalyticsUseCase, action_repository
    )
    kafka_consumer_use_case: KafkaConsumerUseCase = providers.Factory(
        KafkaConsumerUseCase, action_use_case
    )
