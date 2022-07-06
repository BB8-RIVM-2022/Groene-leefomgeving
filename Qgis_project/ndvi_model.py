"""
Model exported as python.
Name : NDVI_model
Group : 
With QGIS : 32403
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterFeatureSink
import processing


class Ndvi_model(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSink('Ndvi_gemeenten_values', 'NDVI_gemeenten_values', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue='C:/Users/hasso/Desktop/Hu/jaar2/BB8/Preventie-gezondheid-en-maatschappij-voor-RIVM/NDVI/Tijdreeks-NDVI-analyse-en-voorspelling/data/NDVI_gemeenten.csv'))
        self.addParameter(QgsProcessingParameterFeatureSink('Ndvi_buurt_values', 'NDVI_buurt_values', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue='C:/Users/hasso/Desktop/Hu/jaar2/BB8/Preventie-gezondheid-en-maatschappij-voor-RIVM/NDVI/Tijdreeks-NDVI-analyse-en-voorspelling/data/NDVI_buurt.csv'))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(2, model_feedback)
        results = {}
        outputs = {}

        # NDVI_buurt_values
        alg_params = {
            'COLUMN_PREFIX': '_',
            'INPUT': 'buurten_fc79eaf7_ddb6_4481_bc56_924b83d71abd',
            'INPUT_RASTER': 'ndvi_e4d76eec_5bf7_4f6c_98a3_b1bd4508f006',
            'RASTER_BAND': 1,
            'STATISTICS': [0,1,2],  # Aantal,Som,Gemiddelde
            'OUTPUT': parameters['Ndvi_buurt_values']
        }
        outputs['Ndvi_buurt_values'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Ndvi_buurt_values'] = outputs['Ndvi_buurt_values']['OUTPUT']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # NDVI_gemeenten_values
        alg_params = {
            'COLUMN_PREFIX': '_',
            'INPUT': 'gemeenten_f41bbe64_7317_4dee_a71e_b9aa81538160',
            'INPUT_RASTER': 'ndvi_e4d76eec_5bf7_4f6c_98a3_b1bd4508f006',
            'RASTER_BAND': 1,
            'STATISTICS': [0,1,2],  # Aantal,Som,Gemiddelde
            'OUTPUT': parameters['Ndvi_gemeenten_values']
        }
        outputs['Ndvi_gemeenten_values'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Ndvi_gemeenten_values'] = outputs['Ndvi_gemeenten_values']['OUTPUT']
        return results

    def name(self):
        return 'NDVI_model'

    def displayName(self):
        return 'NDVI_model'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Ndvi_model()
