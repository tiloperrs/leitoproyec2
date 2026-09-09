from srca.configs import addCommand, Client
from db.mongo_client import MongoDB


@addCommand('global')
def global_(*_, m):

    query = MongoDB().query_user(int(m.from_user.id))

    if query == None:
        return m.reply('Usar el comando $register para el registro.')

    if MongoDB().admin(int(m.from_user.id)) == False:
        return

    data = m.text.split(' ', 1)

    if len(data) < 2 and not m.reply_to_message:
        return m.reply(
            'Ingrese un mensaje correcto.\n'
            '<code>$global mensaje</code>'
        )

    texto = data[1] if len(data) > 1 else ''

    enviados = 0
    errores = 0

    # AQUÍ tenemos que obtener TODOS los usuarios registrados
    usuarios = MongoDB().get_all_users()

    for usuario in usuarios:

        try:

            user_id = usuario['id']

            if m.reply_to_message:

                # FOTO + TEXTO
                if m.reply_to_message.photo:

                    Client.send_photo(
                        chat_id=user_id,
                        photo=m.reply_to_message.photo.file_id,
                        caption=texto
                    )

                else:

                    Client.send_message(
                        chat_id=user_id,
                        text=texto
                    )

            else:

                # SOLO TEXTO
                Client.send_message(
                    chat_id=user_id,
                    text=texto
                )

            enviados += 1

        except Exception as e:

            print(f'Error enviando a {user_id}: {e}')
            errores += 1

    return m.reply(
        f'<b>GLOBAL COMPLETADO ✅</b>\n\n'
        f'📨 Enviados: <code>{enviados}</code>\n'
        f'❌ Errores: <code>{errores}</code>'
    )