package praxis.maven.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;

public class MySQL implements AutoCloseable {
 
    private Connection connection;
    
    public MySQL(String host, Integer port, String base, String user, String pass) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        connection = DriverManager.getConnection("jdbc:mysql://" + host + ":" + port + "/" + base, user, pass);
    }

    @Override
    public void close() throws Exception {
        connection.close();
    }

}
