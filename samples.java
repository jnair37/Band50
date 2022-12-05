import javax.sound.sampled.*;
public class samples 
{
    public static void main(String[] args) 
    {
        playNote(Integer.parseInt(args[0])); //analyzes CLI to determine note input
    }

    public static void playNote(double note) 
    {
        double sampleRate = 44100.0; //defines sample rate
        double hz =  Math.pow(2, (note-4)/12); //interprets note input into frequency
        //calls voids for each piece of kit
        snap(hz, sampleRate); 
        kick(hz, sampleRate); 
        hat(hz, sampleRate); 
        percussion(hz, sampleRate); 
    }

    //produces snap sound
    public static void snap(double hz, double sampleRate) 
    {
        double[] note = new double[231]; //sets up array
        for (int i = 0; i <= 230; i++)
        {
        note[i] = Math.sin(Math.PI*i*(6000-i*3)/sampleRate);
        }
        StdAudio.save("audio/snap.wav", note); //saves snap.wav to audio folder
    }

    //produces kick sound
    public static void kick(double hz, double sampleRate) 
    {
        double[] note = new double[400]; //sets up array
        for (int i = 0; i <= 95; i++)
        {
            note[i] = Math.sin(Math.PI*i*(6000-i*3)/sampleRate); //adds transient to array
        }

        for (int i = 0; i <= 300; i++)
        {
            note[i] = Math.sin(Math.PI*i*(60)/sampleRate); //adds body to array
        }
        StdAudio.save("audio/kick.wav", note); //saves kick.wav to audio folder
    }

    //produces hat sound
    public static void hat(double hz, double sampleRate) 
    {
        double[] note = new double[201]; //sets up array
        for (int i = 0; i <= 200; i++)
        {
            note[i] = Math.sin(Math.PI*i*(16000)/sampleRate); //adds sound to array
        }
        StdAudio.save("audio/hat.wav", note); //saves hat.wav to audio folder
    }

    //produces percussion sound
    public static void percussion(double hz, double sampleRate) 
    {
        double[] note = new double[2001]; //sets up array
        for (int i = 0; i <= 2000; i++)
        { 
            note[i] = Math.sin(Math.PI*i*(10000-i*2)/sampleRate); //adds sound to array
        }
        StdAudio.save("audio/percussion.wav", note); //saves percussion.wav to audio folder
    }
}
