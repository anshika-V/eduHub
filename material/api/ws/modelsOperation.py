from material.models import Test, Question
import io


class TestModelModifier:

    def __init__(self, **kwargs):
        self.test = None
        self.user = None
        # Update class variables according to provided arguments
        self.__dict__.update(kwargs)

    def initilize(self, key):  # initilizing self.test instance
        test = Test.objects.get(pk=key)
        if (test.instructor == self.user):
            self.test = test
            return ({'type': 'connected', 'code': 'is'})
        return({'type': 'error', 'code': 'is', 'message': 'initilization failed, unauthorised access'})

    def testUpdate(self, payload):  # update the test fields
        if (self.test == None):
            return ({'type': 'error', 'code': 'NI'})
        self.test.__dict__.update(payload)
        self.test.save()
        return {'type': 'dataUploaded'}

    def questionUpdate(self, ques):  # Update question fields
        if (self.test == None):
            return ({'type': 'error', 'code': 'NI'})
        dic = {'type': 'saved', 'code': 'SQ'}
        q = None
        if (ques['pk'] == None):  # if new question
            q = Question(parent_test=self.test)
            dic['code'] = 'SNQ'
        else:
            q = Question.objects.get(pk=ques['pk'])
            if (q.parent_test != self.test):
                return({'type': 'error', 'code': 'UA', 'message': "Question dosen't belongs to the initilized test"})
        del ques['fields']['image']  # removing image from the data
        q.__dict__.update(ques['fields'])
        q.save()
        dic['key'] = q.pk
        return (dic)

    def imageUpload(self, payload):
        if (self.test == None):
            return ({'type': 'error', 'code': 'NI'})
        ques = Question.objects.get(pk=payload['key'])
        if (ques.parent_test != self.test):
            return({'type': 'error', 'code': 'UA', 'message': "Question dosen't belongs to the initilized test"})
        ques.image.save(payload['name'], io.BytesIO(
            bytearray(payload['image'])))
        return {'type': 'imageUploaded', 'index': payload['index'], 'image': str(ques.image)}

    def action(self, type, payload):
        if (type == 'questionUpdate'):
            return self.questionUpdate(payload)
        elif (type == 'initilization'):
            return self.initilize(payload)
        elif (type == 'imageUpload'):
            return self.imageUpload(payload)
        elif (type == 'testUpdate'):
            return self.testUpdate(payload)
