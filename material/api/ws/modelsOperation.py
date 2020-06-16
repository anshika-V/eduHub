from material.models import Test, Question
import io


class TestModelModifier:
    test = None
    user = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def initilize(self, key):
        test = Test.objects.get(pk=key)
        if (test.instructor == self.user):
            self.test = test
            return ({'type': 'connected', 'code': 'is'})
        return({'type': 'error', 'code': 'is', 'message': 'initilization failed, unauthorised access'})

    def testUpdate(self, payload):
        if (self.test == None):
            return ({'type': 'error', 'code': 'NI'})
        print('payload:----------')
        print(payload)
        self.test.__dict__.update(payload)
        self.test.save()
        return {'type': 'dataUploaded'}

    def questionUpdate(self, ques):
        if (self.test == None):
            return ({'type': 'error', 'code': 'NI'})
        if (ques['fields']['parent_test'] != self.test.pk):
            return({'type': 'error', 'code': 'UA', 'message': "Question dosen't belongs to the initilized test"})
        dic = {'type': 'saved', 'code': 'SQ'}
        q = None
        if (ques['pk'] == None):
            q = Question(parent_test=self.test)
            dic['code'] = 'SNQ'
        else:
            q = Question.objects.get(pk=ques['pk'])
        del ques['fields']['image']
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
