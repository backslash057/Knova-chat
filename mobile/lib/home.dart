import 'package:flutter/material.dart';


class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Container(
        padding: const EdgeInsets.only(top: 30),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget> [
            const Center(
              child: FractionallySizedBox(
              widthFactor: 0.9,
              child: Image(
                  image: AssetImage("assets/background.png")
                )
              )
            ),
            const Center(
              child: Column(
                children: <Widget> [
                  Text('Welcome !',
                    style: TextStyle(
                      fontSize: 35,
                      fontWeight: FontWeight.bold,
                      color: Colors.pinkAccent
                    ),
                  ),
                  Text("JOIN THE ADVENTURE",
                    style: TextStyle(
                      color: Colors.pinkAccent,
                      fontSize: 12
                    )
                  )
                ]
              )
            ),
            MaterialButton(
              padding: const EdgeInsets.only(left: 70, right: 70, top: 15, bottom: 15),
              onPressed: (){},
              shape: const StadiumBorder(),
              color: Colors.pinkAccent,
              child: const Text("Get Started",
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 18,
                  fontFamily: "Consolas",
                  color: Colors.white
                )
              )
            )
          ]
        ),
      )
    );
  }
}