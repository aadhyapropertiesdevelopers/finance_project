# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Akhila%40910@127.0.0.1:5432/Finance_Project'
    # 'postgresql://postgres:Akhila%40@127.0.0.1:5432/Finance_Project'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Akhila%40910@127.0.0.1:5432/Finance_Project'
    # 'sqlite:///example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   
