package praxis.maven.jdbc;

public class JDBC {
    public static void main(String[] args) throws Exception {
        try (MySQL mysql = new MySQL(null, null, null, null, null)) {
            System.out.println(mysql);
        }
    }
}