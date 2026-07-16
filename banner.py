def grab_banner(sock, port):
    try:
        if port == 80:
            sock.send(b"GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n")

        response = sock.recv(2048).decode(errors="ignore")

        if port == 80:
            lines = response.split("\r\n")

            status = lines[0] if lines else ""
            server = ""

            for line in lines:
                if line.lower().startswith("server:"):
                    server = line
                    break

            if server:
                return f"{status}\n{server}"
            return status

        return response.strip()

    except:
        return "No Banner"