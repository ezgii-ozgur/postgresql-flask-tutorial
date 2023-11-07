from dataclasses import dataclass
# from db_transaction import db
from sqlalchemy import MetaData, Table, Column, ForeignKey, select
from sqlalchemy.types import Integer, String, DateTime, Boolean, Uuid, Unicode
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from alembic import op
import sqlalchemy as sa

Base = declarative_base()


class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, primary_key=True)
    role = Column(String)
    type = Column(String)
    ezgi = Column(String)


    @staticmethod
    def save_db(engine, data):
        try:
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            for i in data:
                # role_name = i["role"]
                # existing_role = session.query(Role).filter_by(role=role_name).first()
                # if existing_role is None :
                my_model = Role(**i)
                session.add(my_model)
                session.commit()
        except Exception as ex:
            print("EXXXXXXXXXX",ex)

    @staticmethod
    def upgrade():
        # Schema migration: add all the new columns.
        op.add_column('role_type', sa.Column('lastname', sa.Unicode(length=50), nullable=True))
        # op.add_column('users', sa.Column('firstname', sa.Unicode(length=50), nullable=True))

        # Data migration: takes a few steps...
        # Declare ORM table views. Note that the view contains old and new columns!
        t_users = sa.Table(
            'Role',
            sa.MetaData(),
            sa.Column('id', sa.Integer),
            sa.Column('role', sa.String),  # Old column.
            sa.Column('lastname', sa.Unicode(length=50)),  # Two new columns.
            # Column('firstname', sa.Unicode(length=50)),
        )

        # Use Alchemy's connection and transaction to noodle over the data.
        connection = op.get_bind()
        # Select all existing names that need migrating.
        results = connection.execute(sa.select([
            t_users.c.id,
            t_users.c.role,
        ])).fetchall()

    # def downgrade():
    #     # Define the downgrade logic here if needed.
    #     pass

    # def upgrade():
    #     # Schema migration: add all the new columns.
    #     op.add_column('role_type', Column('lastname', Unicode(length=50), nullable=True))
    #     # op.add_column('users', Column('firstname', Unicode(length=50), nullable=True))
    #
    #     # Data migration: takes a few steps...
    #     # Declare ORM table views. Note that the view contains old and new columns!
    #     t_users = Table(
    #         'Role',
    #         MetaData(),
    #         Column('id', Integer),
    #         Column('role', String),  # Old column.
    #         Column('lastname', Unicode(length=50)),  # Two new columns.
    #         # Column('firstname', Unicode(length=50)),
    #     )
    #     # Use Alchemy's connection and transaction to noodle over the data.
    #     connection = op.get_bind()
    #     # Select all existing names that need migrating.
    #     results = connection.execute(select([
    #         t_users.c.id,
    #         t_users.c.role,
    #     ])).fetchall()
        # Iterate over all selected data tuples.
        # for id_, name in results:
        #     # Split the existing name into first and last.
        #     firstname, lastname = name.rsplit(' ', 1)
        #     # Update the new columns.
        #     connection.execute(t_users.update().where(t_users.c.id == id_).values(
        #         lastname=lastname,
        #         firstname=firstname,
        #     ))

     # @staticmethod
     # def up
        # try:
        #     with engine.connect() as conn:
        #         meta_data.create_all(conn, checkfirst=False)
        #         Role.patent_table.create(engine)
        #         for item in data:
        #             print("item", item)
        #             insert_statement = Role.patent_table.insert().values(
        #                 _id=item["_id"],
        #                 role=item["role"]
        #             )
        #             print("insert_statement", insert_statement, type(insert_statement))
        #             conn.execute(insert_statement)
        #             conn.commit()
        #     return True
        # except Exception:
        #     return False
