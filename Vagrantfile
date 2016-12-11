# -*- mode: ruby -*-
# vi: set ft=ruby :

ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.require_version '>= 1.5.0'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = 'MattHodge/Windows2012R2Core-WMF5-NOCM'

    config.vm.provider "virtualbox" do |v|
        v.linked_clone = true
    end

    slack_api_token = ENV['SLACK_API_TOKEN']

    presetup = <<SCRIPT
        choco install python -version 3.5.2.20161029 -y
        choco install git.install -y
        choco install nssm -y
        [Environment]::SetEnvironmentVariable("SLACK_API_KEY","#{slack_api_token}","Machine")
        robocopy C:\\vagrant C:\\bot /S /R:1 /W:1 /XF *.log /XD errbot __pycache__ data .git .vagrant
SCRIPT

    installerrbot = <<SCRIPT
        if (!(Get-Service -Name errbot -ErrorAction SilentlyContinue))
        {
            pip install virtualenv
            cd C:\\bot
            virtualenv errbot
            .\\errbot\\Scripts\\activate.ps1
            $env:Path += ";C:\\Program Files\\Git\\bin;C:\\Python35\\Scripts"
            pip install -r requirements.txt
            New-Item -Type Directory -Path 'C:\\bot\\data' -Force
            nssm install errbot C:\\bot\\errbot\\Scripts\\errbot.exe -c C:\\bot\\config.py
            # nssm install errbot C:\\Python35\\Scripts\\errbot.exe -c C:\\bot\\config.py
            nssm set errbot AppDirectory C:\\bot\\
            Start-Service -Name errbot
        }
        else
        {
            cd C:\\bot
            pip install -r requirements.txt
            Restart-Service -Name errbot
        }
SCRIPT

    config.vm.provision 'shell', inline: presetup
    config.vm.provision 'shell', inline: installerrbot
end