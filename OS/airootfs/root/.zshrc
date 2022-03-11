if [[ -f "/root/.configfiles/itdo" ]]
then
    ./.installer.sh
else
    touch /root/.configfiles/itdo
fi
