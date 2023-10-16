# pylint: disable=no-member

import json_manager
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required=True, help='Nombre del usuario')
@click.option('--lastname', required=True, help='Apellido del usuario')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('EL nombre y el apellido son obligatorios')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(
            f"Usuario {name} {lastname} se ha creado satifactoriamente {new_id}")


@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"Usuario {id} no ha sido encontrado")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
@click.option('--name', help="Nombre del usuario")
@click.option('--lastname', help="Apellido del usuario")
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)
    print(f"Usuario {id} actualizado satifactoriamente")


@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"Usuario {id} no ha sido encontrado")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"El usuario {id} ha sido eliminado satifactoriamente")


if __name__ == '__main__':
    cli()
