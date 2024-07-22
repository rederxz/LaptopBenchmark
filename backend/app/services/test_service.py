from app.models import Test


class TestService:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_test(self, user_id, notebook_id, testtag_id, score):
        test = Test(
            user_id=user_id,
            notebook_id=notebook_id,
            testtag_id=testtag_id,
            score=score
        )
        self.db_session.add(test)
        self.db_session.commit()
        return test
