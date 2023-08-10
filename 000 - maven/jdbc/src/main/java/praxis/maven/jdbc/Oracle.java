package praxis.maven.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;

public class Oracle implements AutoCloseable {
 
    private Connection connection;
    
    public Oracle(String host, Integer port, String base, String user, String pass) throws Exception {
        Class.forName("oracle.jdbc.driver.OracleDriver");
        connection = DriverManager.getConnection("jdbc:oracle:thin:@" + host + ":" + port + ":" + base, user, pass);
    }

    @Override
    public void close() throws Exception {
        connection.close();
    }

}
