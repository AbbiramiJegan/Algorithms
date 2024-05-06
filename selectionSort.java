public class SelectionSort {
    public static void selectionSort(int[] A) {
        int n = A.length;
        for (int i = 0; i < n - 1; i++) {
            int minimum = i;
            for (int j = i + 1; j < n; j++) {
                if (A[j] < A[minimum]) {
                    minimum = j;
                }
            }
            int temp = A[i];
            A[i] = A[minimum];
            A[minimum] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        selectionSort(arr);
        System.out.print("Sorted array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
