from survey import AnonymousSurvey

def test_store_single_response():
    """测试能否存储单个答案"""
    question = 'What language did you first learn to speak?'
    my_survey = AnonymousSurvey(question)
    my_survey.store_response('English')
    assert 'English' in my_survey.response

def test_store_three_responses():

    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    responses = ['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.response