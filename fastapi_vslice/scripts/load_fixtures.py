import uuid

import click as click

from fastapi_vslice.models.device import Device
from fastapi_vslice.shared.database import Base, engine, SessionLocal

from faker import Faker
from faker.providers import internet, company

fake = Faker()
fake.add_provider(internet)
fake.add_provider(company)


@click.command()
def load_fixtures():
    click.echo('Load fixtures started')
    Base.metadata.drop_all(bind=engine)
    click.echo('All tables dropped')
    Base.metadata.create_all(bind=engine)
    click.echo('All tables created')

    try:
        with SessionLocal.begin() as db:
            click.echo('Start seeding db with fake data')
            for _ in range(10):
                db.add(
                    Device(
                        id=str(uuid.uuid4()),
                        name=fake.catch_phrase(),
                        address=fake.ipv4_private(),
                        is_active=fake.boolean(),
                    )
                )
            click.echo('Finished seeding db with fake data')
            db.commit()
            click.echo('Fixture loaded successfully')
    except Exception as e:
        click.echo(f'Error: {e}')
        db.rollback()
        click.echo('Error loading fixtures!!!')
    finally:
        db.close()
