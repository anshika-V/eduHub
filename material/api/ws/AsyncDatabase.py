from channels.db import database_sync_to_async
from material.models import Test, TestResult
from django.core import serializers

class AsyncDatabase:            #General async database operations

    @database_sync_to_async
    def getTestFromPk(self, pk):
        test = Test.objects.get(pk=pk)
        return test
    
    @database_sync_to_async
    def saveModelObject(self, obj):
        obj.save()
    
    @database_sync_to_async
    def jsonSerializeModelObject(self, obj_list, **kwargs):
        json_data = serializers.serialize(
            'json', obj_list, **kwargs)
        return json_data

class AsyncDatabaseStudentTest(AsyncDatabase):   #Async database operations specific to student-test consumer need to be inherited bu student test consumer 

    @database_sync_to_async
    def getTestResultsOfUser(self):
        testResults = self.user.testresult_set.all().filter(parent_test=self.test)
        attempted = testResults.exists()
        if (attempted):
            # loading test result to instance variable
            self.test_result = testResults.first()
        return attempted
    
    @database_sync_to_async
    def serialisedQuestionsOfTest(self):
        questions = self.test.question_set.all()
        question_data = serializers.serialize('json', questions)
        return question_data

    async def serializeTest(self):
        json_test = await self.jsonSerializeModelObject([self.test], use_natural_foreign_keys=True)
        return json_test