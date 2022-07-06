"""
Model exported as python.
Name : TasseldCap
Group : HU
With QGIS : 32403
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Tasseldcap(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSink('Gemeente_tct_values', 'Gemeente_tct_values', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue='C:/Users/hasso/Desktop/Hu/jaar2/BB8/Preventie-gezondheid-en-maatschappij-voor-RIVM/NDVI/Tijdreeks-NDVI-analyse-en-voorspelling/data/Tasseld_cap_gemeenten_greenness.csv'))
        self.addParameter(QgsProcessingParameterFeatureSink('Buurt_tct_vaules', 'Buurt_tct_vaules', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue='C:/Users/hasso/Desktop/Hu/jaar2/BB8/Preventie-gezondheid-en-maatschappij-voor-RIVM/NDVI/Tijdreeks-NDVI-analyse-en-voorspelling/data/Tasseld_cap_buurt_greenness.csv'))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(2, model_feedback)
        results = {}
        outputs = {}

        # buurt_tct_vaules
        alg_params = {
            'COLUMN_PREFIX': '_',
            'INPUT': 'buurten_7dd9bba3_3601_4687_9a81_c04be11a305f',
            'INPUT_RASTER': 'Nederland_tasseledcap_7dd58e54_89f2_46ee_83b5_2e926870147e',
            'RASTER_BAND': 2,
            'STATISTICS': [0,1,2],  # Aantal,Som,Gemiddelde
            'OUTPUT': parameters['Buurt_tct_vaules']
        }
        outputs['Buurt_tct_vaules'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Buurt_tct_vaules'] = outputs['Buurt_tct_vaules']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Gemeente_tct_values
        alg_params = {
            'COLUMN_PREFIX': '_',
            'INPUT': 'buurten_7dd9bba3_3601_4687_9a81_c04be11a305f',
            'INPUT_RASTER': 'Nederland_tasseledcap_7dd58e54_89f2_46ee_83b5_2e926870147e',
            'RASTER_BAND': 2,
            'STATISTICS': [0,1,2],  # Aantal,Som,Gemiddelde
            'OUTPUT': parameters['Gemeente_tct_values']
        }
        outputs['Gemeente_tct_values'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Gemeente_tct_values'] = outputs['Gemeente_tct_values']['OUTPUT']
        return results

    def name(self):
        return 'TasseldCap'

    def displayName(self):
        return 'TasseldCap'

    def group(self):
        return 'HU'

    def groupId(self):
        return 'HU'

    def createInstance(self):
        return Tasseldcap()
