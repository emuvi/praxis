package praxis.maven.arch;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ArchTest {

    @Test
    public void testSum() {
        Assertions.assertEquals(2, Arch.sum(1, 1));
    }

}
