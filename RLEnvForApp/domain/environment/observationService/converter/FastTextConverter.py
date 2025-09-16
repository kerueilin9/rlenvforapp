from RLEnvForApp.domain.environment.observationService.converter.FastTextSingleton import \
    FastTextSingleton
from RLEnvForApp.domain.environment.observationService.converter.IConverter import IConverter


class FastTextConverter(IConverter):
    def __init__(self):
        super().__init__()
        FastTextSingleton.getInstance()

    def _convertToListFeature(self, stateElement) -> []:
        word = stateElement.lower()
        return FastTextSingleton.getInstance().getWordVector(word=word)
