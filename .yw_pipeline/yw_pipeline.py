# Youwol application
from youwol.app.environment import YouwolEnvironment
from youwol.app.routers.projects import IPipelineFactory, Pipeline
# Youwol pipelines
from youwol.pipelines.pipeline_python_backend import PipelineConfig, pipeline
# Youwol utilities
from youwol.utils.context import Context


class PipelineFactory(IPipelineFactory):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, context: Context) -> Pipeline:
        config = PipelineConfig(with_tags=["python", "backend", "fastAPI"])
        return await pipeline(config, context)
