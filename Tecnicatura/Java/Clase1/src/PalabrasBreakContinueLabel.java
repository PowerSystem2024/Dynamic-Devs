public class PalabrasBreakContinueLabel {
    public static void main(String[] args) {
        // uso de break
        for (int count = 0; count < 11; count++) {
            if (count % 2 == 0) {
                System.out.println("count = " + count);
                break;
            }
        }

        // uso de continue
        for (int count = 0; count < 11; count++) {
            if (count % 2 != 0) {
                continue;
            }
            System.out.println("count = " + count);
        }

        // uso de label
        outerLoop:
        for (int i = 0; i < 5; i++) {
            innerLoop:
            for (int j = 0; j < 5; j++) {
                if (i != j) {
                    System.out.println("If block values " + i);
                    break outerLoop;
                } else {
                    System.out.println("Else block values " + i);
                    continue innerLoop;
                }
            }
        }
    }
}
