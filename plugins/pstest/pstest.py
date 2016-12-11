from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import winrm

class Pstest(BotPlugin):
    """
    PowerShell test
    """

    def activate(self):
        """
        Triggers on plugin activation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Pstest, self).activate()

    def deactivate(self):
        """
        Triggers on plugin deactivation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Pstest, self).deactivate()

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports

        You should delete it if your plugin doesn't use any configuration like this
        """
        return {'EXAMPLE_KEY_1': "Example value",
                'EXAMPLE_KEY_2': ["Example", "Value"]
               }

    def check_configuration(self, configuration):
        """
        Triggers when the configuration is checked, shortly before activation

        Raise a errbot.utils.ValidationException in case of an error

        You should delete it if you're not using it to override any default behaviour
        """
        super(Pstest, self).check_configuration(configuration)

    def callback_connect(self):
        """
        Triggers when bot is connected

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_message(self, message):
        """
        Triggered for every received message that isn't coming from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_botmessage(self, message):
        """
        Triggered for every message that comes from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    @webhook
    def example_webhook(self, incoming_request):
        """A webhook which simply returns 'Example'"""
        return "Example"

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @arg_botcmd('name', type=str)
    @arg_botcmd('--favorite-number', type=int, unpack_args=False)
    def hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return "Hello {name}".format(name=args.name)
        else:
            return "Hello {name}, I hear your favorite number is {number}".format(
                name=args.name,
                number=args.favorite_number,
            )

    @botcmd(split_args_with=None)
    def sendcard(self, msg, args):
        """Say a card in the chatroom."""
        self.send_card(title='Title + Body',
                       body='text body to put in the card',
                       thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
                       image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                       link='http://www.google.com',
                       fields=(('First Key','Value1'), ('Second Key','Value2')),
                       color='red',
                       in_reply_to=msg)

    @arg_botcmd('computername', type=str)
    @arg_botcmd('--port', dest='port', type=int, default=5985)
    def getmem(self, message, computername=None, port=None):
        """
        Gets memory over WinRM.
        """

        ps_script = """$strComputer = $Host
        Clear
        $RAM = WmiObject Win32_ComputerSystem
        $MB = 1048576

        "Installed Memory: " + [int]($RAM.TotalPhysicalMemory /$MB) + " MB" """


        fullcomputername = computername + ":" + str(port)

        yield "Running command on {fullname}".format(
            fullname = fullcomputername
        )

        s = winrm.Session(fullcomputername, auth=('vagrant', 'vagrant'), transport='ssl', server_cert_validation='ignore')
        r = s.run_ps(ps_script)

        yield "``{stdout}``".format(
            statuscode=r.status_code,
            stdout=r.std_out.decode('utf-8')
        )

    @arg_botcmd('computername', type=str)
    @arg_botcmd('--port', dest='port', type=int, default=5985)
    def getsvc(self, message, computername=None, port=None):
        """
        Gets services over WinRM
        """

        ps_script = """
            Get-Service
        """


        fullcomputername = computername + ":" + str(port)

        yield "Running command on {fullname}".format(
            fullname = fullcomputername
        )

        s = winrm.Session(fullcomputername, auth=('vagrant', 'vagrant'), transport='ssl', server_cert_validation='ignore')
        r = s.run_ps(ps_script)

        yield "{stdout}".format(
            statuscode=r.status_code,
            stdout=r.std_out.decode('utf-8')
        )