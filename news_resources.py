from flask import jsonify
from flask_restful import Resource, abort, reqparse

from data import db_session
from data.news import News


class NewsListResource(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('content', required=True)
        parser.add_argument('is_private', required=True, type=bool)
        parser.add_argument('is_published', required=True, type=bool)
        parser.add_argument('user_id', required=True, type=int)
        self.post_parser = parser


    def get(self):
        session = db_session.create_session()
        news = session.query(News).all()
        result = {
            'news':
                [item.to_dict(only=('title', 'content', 'user.name'))
                 for item in news]
        }
        return jsonify(result)

    def post(self):
        args = self.post_parser.parse_args()
        session = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_private=args['is_private']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class NewsResources(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        return jsonify({
            'news': news.to_dict(only=('id', 'title', 'content', 'user_id', 'is_private'))
        })

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})

