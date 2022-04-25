from background import editor
from background import generate
from background import backstuff
import argparse
from data import about
from data.banners import banner
class main:

    def __init__(self):


        parser = argparse.ArgumentParser()
        parser.add_argument("--server", action="store_true", help="server")
        parser.add_argument("--client", action="store_true", help="client")
        parser.add_argument("-host", "--host", help="Host")
        parser.add_argument("-port", "--port", help="Port")

        args = parser.parse_args()
        if args.server:
            self.edit(args.host, args.port)
            self.run_server(args.host, args.port)
        elif args.client:
            self.edit(args.host, args.port)

            print("Generating client exe please wait...")

            if self.generate_client() == 0:
                print("Done generating client exe, check dist folder.")
            else:
                print("Failed to generate.")

    def run_server(self, host: str, port: int):

        from server import server

        mbanner = banner.main_banner(host, port, about.__version__, about.__name__)
        backstuff.clear()
        print(mbanner)
        server = server.server(host, port)
        server.main()

    def generate_client(self):
        generator = generate.generator()
        return generator.to_exe("client\client.py")



    def edit(self, host: str, port: str):
        editor.edit_basicvar("data/basic.py", "HOST", host)
        editor.edit_basicvar("data/basic.py", "PORT", int(port))
        return

if __name__ == "__main__":

    main()