from interfaces_usuario.menu import (
    mostrar_menu,
    registrar_usuario,
    login,
    opcion_get_posts_comments,
    opcion_post,
    opcion_put,
    opcion_delete
)

def main():
    logueado = False

    while True:
        mostrar_menu()
        op = input("Opción: ").strip()

        if op == "1":
            registrar_usuario()

        elif op == "2":
            logueado = login()

        elif op == "3":
            if not logueado:
                print("Debe iniciar sesión primero.")
                continue
            opcion_get_posts_comments()

        elif op == "4":
            if not logueado:
                print("Debe iniciar sesión primero.")
                continue
            opcion_post()

        elif op == "5":
            if not logueado:
                print("Debe iniciar sesión primero.")
                continue
            opcion_put()

        elif op == "6":
            if not logueado:
                print("Debe iniciar sesión primero.")
                continue
            opcion_delete()

        elif op == "0":
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
